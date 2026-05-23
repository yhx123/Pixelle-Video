import asyncio
import os
import sys
from pathlib import Path

# 将项目根目录加入到 Python 模块搜索路径中
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from pixelle_video.services.frame_html import HTMLFrameGenerator
from loguru import logger

async def test_knowledge_template():
    logger.info("========== 开始测试 墨绿考点知识分享模板 (image_zsb_knowledge.html) ==========")
    template_path = project_root / "templates" / "1080x1920" / "image_zsb_knowledge.html"
    
    # 模拟真实高数考点内容
    title = "高等数学核心考点"
    text = "【核心要点一】极限的求法与导数的应用。\n【核心要点二】牢记洛必达法则及泰勒展开式，这是江西专升本高数必考题型，占比高达15%！\n【提分秘籍】务必多刷真题，攻克不定式极限！"
    
    # 使用一张精美公开背景作为配图演示
    sample_image = "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?q=80&w=1024&auto=format&fit=crop"
    
    output_img_path = str(project_root / "scratch" / "test_zsb_knowledge.png")
    
    generator = HTMLFrameGenerator(str(template_path))
    
    # 注入额外的模板变量
    ext_data = {
        "countdown": "江西专升本 • 倒计时 60 天",
        "category": "高等数学",
        "author": "壹格专升本",
        "describe": "江西专升本一站式上岸品牌。政策解读 丨 真题刷题 丨 备考规划",
        "brand": "壹格专升本"
    }
    
    await generator.generate_frame(
        title=title,
        text=text,
        image=sample_image,
        ext=ext_data,
        output_path=output_img_path
    )
    logger.info(f"墨绿知识模板渲染成功！保存路径为: {output_img_path}")

async def test_consult_template():
    logger.info("========== 开始测试 红橙政策速递模板 (static_zsb_consult.html) ==========")
    template_path = project_root / "templates" / "1080x1920" / "static_zsb_consult.html"
    
    # 模拟江西专升本最新的报考咨询速报
    title = "江西专升本重大政策"
    text = "江西省教育考试院最新通知：\n1. 2026年江西专升本报名时间确定为下月开始！\n2. 统招招生名额保持稳定，部分重点本科院校扩大招生！\n3. 江西师大、南昌航大等热门院校报考指南已发布，请点击壹格备考资料包查看完整对比数据。"
    
    output_img_path = str(project_root / "scratch" / "test_zsb_consult.png")
    
    generator = HTMLFrameGenerator(str(template_path))
    
    # 注入额外的模板变量
    ext_data = {
        "badge": "政策速递",
        "slogan": "壹格专升本江西站 • 助您再上一格",
        "author": "壹格专升本",
        "describe": "江西专升本官方政策一站式速递解读，专业数据，直通本科",
        "brand": "壹格专升本"
    }
    
    # 因为 static 模板不需要 AI 配图，我们传入空图片或者占位图片
    await generator.generate_frame(
        title=title,
        text=text,
        image="",
        ext=ext_data,
        output_path=output_img_path
    )
    logger.info(f"红橙咨询模板渲染成功！保存路径为: {output_img_path}")

async def main():
    try:
        # 执行测试
        await test_knowledge_template()
        await test_consult_template()
    finally:
        # 确保关闭 Playwright 共享浏览器资源，防止阻塞程序挂起
        await HTMLFrameGenerator.close_browser()

if __name__ == "__main__":
    asyncio.run(main())
