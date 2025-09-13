import requests
import pandas as pd
import json
import schedule
import time
import os
from datetime import datetime


class JisiluBondSpider:
    def __init__(self):
        self.session = requests.Session()
        self.setup_headers()

    def setup_headers(self):
        """设置请求头和cookies（已内置）"""
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.jisilu.cn/web/data/cb/list',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

        # 内置cookies信息
        self.cookies = {
            'Hm_lpvt_164fe01b1433a19b5075': '1757430917',
            'Hm_lvt_164fe01b1433a19b50759': '1757429395',
            'HMACCOUNT': 'B48074E612E08101',
            'kbz_newcookie': '1',
            'kbzw__Session': '1bolbrapnsvdgi8ulkl7louui0',
            'kbzw__user_login': '70bd08_P1ebax9aXwzotlquvpqqaooKvpuXK7N_u0ejF1dSe2pqpxKWv1suuz6jDqpTd26XaldGX2LGunNqe2ZapxNiYrqXW2cXS1qCbqqoom6ezmLKgubXOvp-qrJ6woKmbq5evmK6ltrG_0aTC'
        }

    def fetch_bond_data(self):
        """获取可转债数据（API信息已内置）"""
        # 内置API地址
        url = 'https://www.jisilu.cn/webapi/cb/list/'

        # 内置请求参数
        params = {
            'is_search': 'N',
            'market_cd[]': ['shmb', 'szmb'],
            'btype': 'C',
            'listed': 'Y',
            'rp': '50',
            'page': '1'
        }

        try:
            print("🔄 正在请求可转债数据...")
            response = self.session.get(
                url,
                headers=self.headers,
                params=params,
                cookies=self.cookies,
                timeout=15
            )

            print(f"📊 响应状态码: {response.status_code}")

            if response.status_code == 200:
                data = response.json()
                print("✅ 数据获取成功！")
                return data
            else:
                print(f"❌ 请求失败，状态码: {response.status_code}")
                return None

        except Exception as e:
            print(f"❌ 请求异常: {e}")
            return None

    def parse_data(self, data):
        """解析数据"""
        if not data or 'data' not in data:
            print("❌ 数据格式错误")
            return None

        try:
            print("🔍 开始解析数据...")
            bond_data = data['data']

            # 创建数据列表
            bond_list = []
            for bond in bond_data:
                bond_list.append({
                    '债券代码': bond.get('bond_id', ''),
                    '债券名称': bond.get('bond_nm', ''),
                    '当前价格': bond.get('price', ''),
                    '涨跌幅': bond.get('increase_rt', ''),
                    '溢价率': bond.get('premium_rt', ''),
                    '双低值': bond.get('dblow', ''),
                    '转股价值': bond.get('convert_value', ''),
                    '成交量': bond.get('volume', ''),
                    '评级': bond.get('rating_cd', ''),
                    '剩余规模': bond.get('curr_iss_amt', ''),
                    '到期收益率': bond.get('ytm_rt', ''),
                    '正股代码': bond.get('stock_id', ''),
                    '正股名称': bond.get('stock_nm', ''),
                    '正股价格': bond.get('sprice', ''),
                    '正股涨跌幅': bond.get('sincrease_rt', ''),
                    '转股价': bond.get('convert_price', ''),
                    '剩余年限': bond.get('year_left', ''),
                    '强赎状态': '是' if bond.get('redeem_dt') else '否',
                    '强赎日期': bond.get('redeem_dt', ''),
                    '上市日期': bond.get('list_dt', ''),
                    '到期日期': bond.get('maturity_dt', '')
                })

            df = pd.DataFrame(bond_list)

            # 数据清洗
            print("🧹 进行数据清洗...")

            # 处理百分比字段
            percent_columns = ['涨跌幅', '溢价率', '到期收益率', '正股涨跌幅']
            for col in percent_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            # 处理数值字段
            numeric_columns = ['当前价格', '双低值', '转股价值', '成交量', '剩余规模', '正股价格', '转股价', '剩余年限']
            for col in numeric_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            # 添加时间信息
            current_time = datetime.now()
            df['采集时间'] = current_time.strftime('%Y-%m-%d %H:%M:%S')
            df['数据日期'] = current_time.strftime('%Y-%m-%d')

            print(f"✅ 解析完成，共 {len(df)} 条记录")
            return df

        except Exception as e:
            print(f"❌ 数据解析失败: {e}")
            import traceback
            traceback.print_exc()
            return None

    def save_to_excel(self, df, filename=None):
        """保存到Excel"""
        if df is None or df.empty:
            print("❌ 无数据可保存")
            return False

        # 创建数据目录
        os.makedirs('bond_data', exist_ok=True)

        if filename is None:
            current_date = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'jisilu_bond_data_{current_date}.xlsx'

        filepath = os.path.join('bond_data', filename)

        try:
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='可转债数据', index=False)

                # 设置列宽
                worksheet = writer.sheets['可转债数据']
                for column in worksheet.columns:
                    max_length = 0
                    column_letter = column[0].column_letter
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = min(max_length + 2, 30)
                    worksheet.column_dimensions[column_letter].width = adjusted_width

            print(f"💾 数据已保存至: {filepath}")
            print(f"📊 共保存 {len(df)} 条记录")

            # 显示文件大小
            file_size = os.path.getsize(filepath) / 1024
            print(f"📁 文件大小: {file_size:.2f} KB")

            return True

        except Exception as e:
            print(f"❌ 保存失败: {e}")
            return False

    def setup_scheduler(self, schedule_time="09:00"):
        """设置定时任务"""
        # 每天指定时间执行
        schedule.every().day.at(schedule_time).do(self.daily_task)

        print(f"⏰ 定时任务已设置，每天 {schedule_time} 自动采集数据")
        print("🔄 程序运行中，按 Ctrl+C 退出...")

        while True:
            schedule.run_pending()
            time.sleep(60)

    def daily_task(self):
        """每日任务"""
        print(f"\n{'=' * 60}")
        print(f"📅 开始执行每日任务 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'=' * 60}")

        data = self.fetch_bond_data()

        if data:
            df = self.parse_data(data)
            if df is not None:
                filename = f'jisilu_bond_data_{datetime.now().strftime("%Y%m%d")}.xlsx'
                self.save_to_excel(df, filename)

                # 显示数据概览
                print(f"\n📋 今日数据概览:")
                print(f"💰 平均价格: {df['当前价格'].mean():.2f}")
                print(f"📈 平均溢价率: {df['溢价率'].mean():.2f}%")
                print(f"🔺 上涨数量: {len(df[df['涨跌幅'] > 0])}")
                print(f"🔻 下跌数量: {len(df[df['涨跌幅'] < 0])}")
            else:
                print("❌ 数据解析失败")
        else:
            print("❌ 数据获取失败")

        print(f"✅ 每日任务完成 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def show_menu():
    """显示菜单"""
    print("=" * 60)
    print("📊 集思录可转债数据采集程序")
    print("=" * 60)
    print("1. 🚀 立即执行单次采集")
    print("2. ⏰ 启动定时任务（每天9点自动采集）")
    print("3. ⚙️  自定义定时时间")
    print("4. 📁 查看历史数据文件")
    print("5. ❌ 退出程序")
    print("=" * 60)


def list_data_files():
    """列出历史数据文件"""
    data_dir = 'bond_data'
    if os.path.exists(data_dir) and os.listdir(data_dir):
        print(f"\n📁 历史数据文件列表:")
        files = os.listdir(data_dir)
        for i, file in enumerate(files, 1):
            file_path = os.path.join(data_dir, file)
            file_size = os.path.getsize(file_path) / 1024
            file_time = datetime.fromtimestamp(os.path.getctime(file_path))
            print(f"{i}. {file} ({file_size:.1f} KB, {file_time.strftime('%Y-%m-%d %H:%M')})")
    else:
        print("\n📁 暂无历史数据文件")


def main():
    """主函数"""
    spider = JisiluBondSpider()

    while True:
        show_menu()
        choice = input("请选择操作 (1-5): ").strip()

        if choice == '1':
            # 立即执行单次采集
            print("\n🚀 开始执行单次数据采集...")
            data = spider.fetch_bond_data()

            if data:
                df = spider.parse_data(data)
                if df is not None:
                    success = spider.save_to_excel(df)
                    if success:
                        print("\n" + "=" * 50)
                        print("📋 数据预览 (前5行):")
                        print("=" * 50)
                        print(
                            df[['债券代码', '债券名称', '当前价格', '涨跌幅', '溢价率']].head().to_string(index=False))
            input("\n按回车键返回菜单...")

        elif choice == '2':
            # 启动定时任务（默认9点）
            print("\n⏰ 启动定时任务，每天9:00自动采集...")
            spider.setup_scheduler("09:00")

        elif choice == '3':
            # 自定义定时时间
            custom_time = input("请输入定时时间 (格式: HH:MM，如09:30): ").strip()
            if len(custom_time) == 5 and custom_time[2] == ':':
                print(f"\n⏰ 启动定时任务，每天 {custom_time} 自动采集...")
                spider.setup_scheduler(custom_time)
            else:
                print("❌ 时间格式错误，请使用 HH:MM 格式")
                time.sleep(2)

        elif choice == '4':
            # 查看历史文件
            list_data_files()
            input("\n按回车键返回菜单...")

        elif choice == '5':
            # 退出程序
            print("👋 感谢使用，程序退出！")
            break

        else:
            print("❌ 无效选择，请重新输入")
            time.sleep(1)


if __name__ == '__main__':
    # 检查并安装必要依赖
    try:
        import requests
        import pandas
        import schedule
        import openpyxl
    except ImportError:
        print("📦 正在安装所需依赖...")
        os.system('pip install requests pandas schedule openpyxl')
        print("✅ 依赖安装完成，请重新运行程序")
        exit()

main()