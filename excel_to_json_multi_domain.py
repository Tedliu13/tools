
import pandas as pd
import json

def convert_excel_to_json(excel_path='tools.xlsx', json_path='tools_multi_domain.json'):
    df = pd.read_excel(excel_path)
    df = df.fillna("")

    # 將「適合領域」以頓號分隔並轉為 list
    df["適合領域"] = df["適合領域"].apply(lambda x: [d.strip() for d in str(x).split("、") if d.strip()])

    tools = []
    for _, row in df.iterrows():
        tools.append({
            "name": row["工具名稱"],
            "description": row["工具簡介"],
            "image": row["圖片檔名"],
            "download": row["下載位置"],
            "doc": row["說明文件"],
            "interface": row["工具介面"],
            "domain": row["適合領域"],
            "release": row["釋出時間"],
            "status": row["使用狀態"],
            "note": row["備註"]
        })

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, ensure_ascii=False, indent=2)

    print(f"✅ 已成功轉換為 JSON：{json_path}")

if __name__ == "__main__":
    convert_excel_to_json()
