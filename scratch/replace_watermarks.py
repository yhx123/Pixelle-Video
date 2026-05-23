# -*- coding: utf-8 -*-
"""
批量替换 templates 目录下所有 HTML 模板中的默认品牌水印
将 {{brand=Pixelle-Video}} 替换为 {{brand=壹格专升本}}
"""
import os

def main():
    templates_dir = "/Users/yanghongxing/Downloads/project/Pixelle-Video/templates"
    count = 0
    
    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # 执行替换
                new_content = content.replace("{{brand=Pixelle-Video}}", "{{brand=壹格专升本}}")
                
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✅ 已成功替换文件中的水印: {file_path}")
                    count += 1
                    
    print(f"🎉 替换完成，共修改了 {count} 个模板文件")

if __name__ == "__main__":
    main()
