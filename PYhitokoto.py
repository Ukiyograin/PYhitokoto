import json
import urllib.request
import urllib.parse

def get_hitokoto():
    """使用urllib获取一言语录"""
    try:
        # 一言API地址
        url = "https://v1.hitokoto.cn/"
        
        # 创建请求
        req = urllib.request.Request(url)
        
        # 发送请求并获取响应
        with urllib.request.urlopen(req, timeout=10) as response:
            # 读取响应内容
            data = response.read()
            # 解码JSON
            result = json.loads(data.decode('utf-8'))
            
            return {
                'hitokoto': result['hitokoto'],
                'from': result.get('from', ''),
                'from_who': result.get('from_who', ''),
                'type': result['type']
            }
            
    except Exception as e:
        print(f"获取失败: {e}")
        return None

def main():
    """主程序"""
    print("=" * 50)
    print("一言语录获取工具")
    print("=" * 50)
    
    while True:
        try:
            print("\n1. 获取随机语录")
            print("2. 退出程序")
            choice = input("\n请选择操作 (1/2): ").strip()
            
            if choice == '1':
                print("\n正在获取语录...")
                quote = get_hitokoto()
                
                if quote:
                    print("\n" + "=" * 40)
                    print(f"「{quote['hitokoto']}」\n")
                    
                    if quote['from_who'] or quote['from']:
                        print("——", end="")
                        if quote['from_who']:
                            print(f" {quote['from_who']}", end="")
                        if quote['from']:
                            if quote['from_who']:
                                print(f" 《{quote['from']}》")
                            else:
                                print(f" 《{quote['from']}》")
                        else:
                            print()
                    
                    print(f"分类: {quote['type']}")
                    print("=" * 40)
                else:
                    print("获取失败，请检查网络连接！")
                    
            elif choice == '2':
                print("\n感谢使用，再见！")
                break
            else:
                print("无效选择，请输入1或2！")
                
        except KeyboardInterrupt:
            print("\n\n程序被中断，再见！")
            break
        except Exception as e:
            print(f"发生错误: {e}")

if __name__ == "__main__":
    main()