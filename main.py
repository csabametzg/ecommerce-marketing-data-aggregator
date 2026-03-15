import os
import pandas as pd


ORDERS_FILE = "data/orders.csv"
EMAIL_FILE = "data/email_campaigns.csv"
OUTPUT_FILE = "output/summary_report.txt"


def huf(amount: float) -> str:
    return f"{int(round(amount)):,} Ft".replace(",", " ")


def load_data():
    orders_df = pd.read_csv(ORDERS_FILE)
    email_df = pd.read_csv(EMAIL_FILE)

    orders_df["order_date"] = pd.to_datetime(orders_df["order_date"])
    email_df["campaign_date"] = pd.to_datetime(email_df["campaign_date"])

    return orders_df, email_df


def calculate_orders_summary(orders_df: pd.DataFrame) -> dict:
    total_orders = len(orders_df)
    total_revenue = orders_df["total_amount"].sum()
    total_items_sold = orders_df["quantity"].sum()

    top_product_series = (
        orders_df.groupby("product_name")["quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    top_product = top_product_series.index[0] if not top_product_series.empty else "N/A"
    average_order_value = total_revenue / total_orders if total_orders > 0 else 0

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "total_items_sold": total_items_sold,
        "top_product": top_product,
        "average_order_value": average_order_value,
    }


def calculate_email_summary(email_df: pd.DataFrame) -> dict:
    total_campaigns = len(email_df)
    total_emails_sent = email_df["emails_sent"].sum()
    total_opens = email_df["opens"].sum()
    total_clicks = email_df["clicks"].sum()
    total_unsubscribed = email_df["unsubscribed"].sum()

    open_rate = (total_opens / total_emails_sent * 100) if total_emails_sent > 0 else 0
    click_rate = (total_clicks / total_emails_sent * 100) if total_emails_sent > 0 else 0

    return {
        "total_campaigns": total_campaigns,
        "total_emails_sent": total_emails_sent,
        "total_opens": total_opens,
        "total_clicks": total_clicks,
        "total_unsubscribed": total_unsubscribed,
        "open_rate": open_rate,
        "click_rate": click_rate,
    }


def get_top_campaigns_by_open_rate(email_df: pd.DataFrame, top_n: int = 5) -> list:
    df = email_df.copy()
    df = df[df["emails_sent"] > 0].copy()

    df["open_rate"] = (df["opens"] / df["emails_sent"]) * 100
    df = df.sort_values(by="open_rate", ascending=False)

    top_campaigns = []
    for _, row in df.head(top_n).iterrows():
        top_campaigns.append({
            "campaign_name": row["campaign_name"],
            "open_rate": row["open_rate"],
        })

    return top_campaigns


def get_top_campaigns_by_click_rate(email_df: pd.DataFrame, top_n: int = 5) -> list:
    df = email_df.copy()
    df = df[df["emails_sent"] > 0].copy()

    df["click_rate"] = (df["clicks"] / df["emails_sent"]) * 100
    df = df.sort_values(by="click_rate", ascending=False)

    top_campaigns = []
    for _, row in df.head(top_n).iterrows():
        top_campaigns.append({
            "campaign_name": row["campaign_name"],
            "click_rate": row["click_rate"],
        })

    return top_campaigns


def get_best_campaign(email_df: pd.DataFrame) -> dict:
    df = email_df.copy()
    df = df[df["emails_sent"] > 0].copy()

    df["open_rate"] = (df["opens"] / df["emails_sent"]) * 100
    df["click_rate"] = (df["clicks"] / df["emails_sent"]) * 100

    best_row = df.sort_values(by="open_rate", ascending=False).iloc[0]

    return {
        "campaign_name": best_row["campaign_name"],
        "open_rate": best_row["open_rate"],
        "click_rate": best_row["click_rate"],
        "emails_sent": best_row["emails_sent"],
    }


def build_report(
    orders_summary: dict,
    email_summary: dict,
    top_open_campaigns: list,
    top_click_campaigns: list,
    best_campaign: dict
) -> str:

    avg_clicks_per_order = (
        email_summary["total_clicks"] / orders_summary["total_orders"]
        if orders_summary["total_orders"] > 0 else 0
    )

    sales_performance_per_click = (
        orders_summary["total_orders"] / email_summary["total_clicks"] * 100
        if email_summary["total_clicks"] > 0 else 0
    )

    top_open_campaigns_text = ""
    for campaign in top_open_campaigns:
        top_open_campaigns_text += (
            f'- {campaign["campaign_name"]} -> {campaign["open_rate"]:.2f}% open rate\n'
        )

    top_click_campaigns_text = ""
    for campaign in top_click_campaigns:
        top_click_campaigns_text += (
            f'- {campaign["campaign_name"]} -> {campaign["click_rate"]:.2f}% click rate\n'
        )

    report = f"""====== E-commerce and Marketing Summary Report ======

Orders summary
--------------
Total orders: {orders_summary["total_orders"]}
Total revenue: {huf(orders_summary["total_revenue"])}
Total items sold: {int(orders_summary["total_items_sold"])}
Top product: {orders_summary["top_product"]}
Average order value: {huf(orders_summary["average_order_value"])}

Email campaign summary
----------------------
Campaigns sent: {email_summary["total_campaigns"]}
Emails sent: {int(email_summary["total_emails_sent"])}
Total opens: {int(email_summary["total_opens"])}
Total clicks: {int(email_summary["total_clicks"])}
Total unsubscribed: {int(email_summary["total_unsubscribed"])}

Calculated metrics
------------------
Open rate: {email_summary["open_rate"]:.2f}%
Click rate: {email_summary["click_rate"]:.2f}%
Sales performance / click: {sales_performance_per_click:.2f}%
Average clicks per order: {avg_clicks_per_order:.2f}%


Best campaign
-------------
{best_campaign["campaign_name"]}
- Open rate: {best_campaign["open_rate"]:.2f}%
- Click rate: {best_campaign["click_rate"]:.2f}%
- Emails sent: {int(best_campaign["emails_sent"])}

Top performing campaigns by open rate
-------------------------------------
{top_open_campaigns_text}
Top performing campaigns by click rate
--------------------------------------
{top_click_campaigns_text}
"""
    return report


def save_report(report_text: str):
    os.makedirs("output", exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report_text)


def main():
    orders_df, email_df = load_data()

    orders_summary = calculate_orders_summary(orders_df)
    email_summary = calculate_email_summary(email_df)
    top_open_campaigns = get_top_campaigns_by_open_rate(email_df)
    top_click_campaigns = get_top_campaigns_by_click_rate(email_df)
    best_campaign = get_best_campaign(email_df)

    report_text = build_report(
        orders_summary,
        email_summary,
        top_open_campaigns,
        top_click_campaigns,
        best_campaign
    )

    save_report(report_text)

    print(report_text)
    print(f"Report saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
