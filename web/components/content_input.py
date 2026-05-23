# Copyright (C) 2025 AIDC-AI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Content input components for web UI (left column)
"""

import streamlit as st

from web.i18n import tr
from web.utils.async_helpers import get_project_version


def render_content_input():
    """Render content input section (left column) with batch support"""
    with st.container(border=True):
        st.markdown(f"**{tr('section.content_input')}**")
        
        # ====================================================================
        # Step 1: Batch mode toggle (highest priority)
        # ====================================================================
        batch_mode = st.checkbox(
            tr("batch.mode_label"),
            value=False,
            help=tr("batch.mode_help")
        )
        
        if not batch_mode:
            # ================================================================
            # Single task mode (original logic, unchanged)
            # ================================================================
            # Processing mode selection
            mode = st.radio(
                "Processing Mode",
                ["generate", "fixed"],
                horizontal=True,
                format_func=lambda x: tr(f"mode.{x}"),
                label_visibility="collapsed"
            )
            
            # Text input (unified for both modes)
            split_mode = "paragraph"
            if mode == "generate":
                text_placeholder = tr("input.topic_placeholder")
                text_height = 120
                text_help = tr("input.text_help_generate")
                
                text = st.text_area(
                    tr("input.text"),
                    placeholder=text_placeholder,
                    height=text_height,
                    help=text_help
                )
            else:
                # Fixed mode: dynamic list-based multi-row input with smart layout
                st.info(tr("input.fixed_format_hint"))
                
                # Initialize state with 7 premium "壹格专升本" video scenes
                if "fixed_scenes_count" not in st.session_state:
                    st.session_state.fixed_scenes_count = 7
                    
                    # 预设的专升本分镜旁白与自定义生图提示词 (深度融入 LOCAL_MODEL_GUIDE)
                    default_scenes = [
                        {
                            "narration": "2027届专升本，现在才开始起步，是不是已经晚了？先给结论：不晚，而且节奏刚刚好！10个月时间足够你从零逆袭！",
                            "prompt": "cozy anime style, Ghibli Art, a warm desk lamp lighting up a student looking anxious at a desk with textbooks at night, nostalgic and emotional atmosphere, slow camera zoom in, soft shadows --ar 9:16"
                        },
                        {
                            "narration": "我们务实地算笔时间账：扣除在校期、期末考试和懈怠期，10个月你大约有700到900小时的有效学习时间，足够完成三轮系统复习！",
                            "prompt": "flat illustration, vector, vector illustration, minimalist, vibrant teal and orange gradient background, a glowing glass hourglass and calendar pages turning, clean white lines, smooth motion --ar 9:16"
                        },
                        {
                            "narration": "先看你站在哪：零基础同学，首要任务是每天背30个单词建立学习节奏；有概念同学，要用一套真题快速评估，补齐弱项短板！",
                            "prompt": "flat illustration, vector, vector illustration, minimalist, vibrant blue and purple gradient background, two athletic running shoes on a clean white starting line, modern flat vector graphic --ar 9:16"
                        },
                        {
                            "narration": "5到7月公共课先动起来：英语最早启动，词汇雷打不动；政治紧随其后搭建大纲框架；信息技术稍晚，重点攻克选择题和Office操作！",
                            "prompt": "flat illustration, vector, vector illustration, minimalist, vibrant yellow and orange gradient background, a neat desk with English grammar books, a glowing blue gear symbol on a laptop screen, clean white lines --ar 9:16"
                        },
                        {
                            "narration": "记住，千万别一上来就四科齐开！5到6月先翻目录做预学习，等到7月暑假，再集中火力开启专业课的第一轮系统复习。",
                            "prompt": "Claymation, Q-version 3D clay style, a cute and friendly clay male student sitting happily at a sunny summer desk, holding a big red textbook titled \"Higher Math\", warm lighting --ar 9:16"
                        },
                        {
                            "narration": "现在就可以做三件事：第一，确认你的招考类别和考科；第二，拿一套2026年真题限时感受难度；第三，制定一个『100天跑起来』的计划！",
                            "prompt": "Claymation, a beautiful modern study planner on a cozy wooden desk, three bright green checklists marked done, a cute mini coffee mug, soft warm volumetric window light --ar 9:16"
                        },
                        {
                            "narration": "专升本不是短跑，而是跑赢终点的长跑。关注壹格上岸，回复『2027』领取完整备考规划，帮你少走弯路，一站式成功上岸！",
                            "prompt": "cozy anime style, Ghibli Art, a scenic road leading towards a bright glowing university campus on a sunny morning, warm light, optimistic and hopeful mood, camera panning forward slowly --ar 9:16"
                        }
                    ]
                    
                    for idx, scene in enumerate(default_scenes):
                        st.session_state[f"fixed_narration_{idx}"] = scene["narration"]
                        st.session_state[f"fixed_prompt_{idx}"] = scene["prompt"]
                
                # Render list
                for i in range(st.session_state.fixed_scenes_count):
                    # We want each row to be: [Narration (5), Image Prompt (5), Delete button (1)]
                    col1, col2, col3 = st.columns([5, 5, 1])
                    
                    with col1:
                        # Make first row label visible, others collapsed for neat grid
                        label_vis = "visible" if i == 0 else "collapsed"
                        st.text_input(
                            label=tr("input.narration_label"),
                            key=f"fixed_narration_{i}",
                            placeholder=tr("input.narration_placeholder"),
                            label_visibility=label_vis
                        )
                        
                    with col2:
                        st.text_input(
                            label=tr("input.prompt_label"),
                            key=f"fixed_prompt_{i}",
                            placeholder=tr("input.prompt_placeholder"),
                            label_visibility=label_vis
                        )
                        
                    with col3:
                        # Align delete button with inputs vertically
                        if i == 0:
                            # Align first row with label height
                            st.markdown('<div style="height: 28px;"></div>', unsafe_allow_html=True)
                            
                        if st.button("🗑️", key=f"del_btn_{i}", help="删除此分镜", use_container_width=True):
                            # Shift all subsequent scenes up
                            for idx in range(i, st.session_state.fixed_scenes_count - 1):
                                st.session_state[f"fixed_narration_{idx}"] = st.session_state.get(f"fixed_narration_{idx+1}", "")
                                st.session_state[f"fixed_prompt_{idx}"] = st.session_state.get(f"fixed_prompt_{idx+1}", "")
                            
                            # Clean up the last one
                            last_idx = st.session_state.fixed_scenes_count - 1
                            if f"fixed_narration_{last_idx}" in st.session_state:
                                del st.session_state[f"fixed_narration_{last_idx}"]
                            if f"fixed_prompt_{last_idx}" in st.session_state:
                                del st.session_state[f"fixed_prompt_{last_idx}"]
                                
                            st.session_state.fixed_scenes_count = max(1, st.session_state.fixed_scenes_count - 1)
                            st.rerun()
                
                # Add row button
                if st.button(tr("input.add_scene"), use_container_width=True):
                    st.session_state.fixed_scenes_count += 1
                    st.rerun()
                
                # Assemble text format compatible with backend
                valid_blocks = []
                for i in range(st.session_state.fixed_scenes_count):
                    nar = st.session_state.get(f"fixed_narration_{i}", "").strip()
                    prt = st.session_state.get(f"fixed_prompt_{i}", "").strip()
                    if nar or prt:
                        block_lines = []
                        if nar:
                            block_lines.append(nar)
                        else:
                            block_lines.append("...")
                        if prt:
                            block_lines.append(f"提示词：{prt}")
                        valid_blocks.append("\n".join(block_lines))
                text = "\n\n".join(valid_blocks)
            
            # Title input (optional for both modes)
            title = st.text_input(
                tr("input.title"),
                placeholder=tr("input.title_placeholder"),
                help=tr("input.title_help")
            )
            
            # Number of scenes (only show in generate mode)
            if mode == "generate":
                n_scenes = st.slider(
                    tr("video.frames"),
                    min_value=3,
                    max_value=30,
                    value=5,
                    help=tr("video.frames_help"),
                    label_visibility="collapsed"
                )
                st.caption(tr("video.frames_label", n=n_scenes))
            else:
                # Fixed mode: n_scenes is ignored, set default value
                n_scenes = 5
                st.info(tr("video.frames_fixed_mode_hint"))
            
            return {
                "batch_mode": False,
                "mode": mode,
                "text": text,
                "title": title,
                "n_scenes": n_scenes,
                "split_mode": split_mode
            }
        
        else:
            # ================================================================
            # Batch mode (simplified YAGNI version)
            # ================================================================
            st.markdown(f"**{tr('batch.section_title')}**")
            
            # Batch rules info
            st.info(f"""
**{tr('batch.rules_title')}**
- ✅ {tr('batch.rule_1')}
- ✅ {tr('batch.rule_2')}
- ✅ {tr('batch.rule_3')}
            """)
            
            # Batch topics input
            text_input = st.text_area(
                tr("batch.topics_label"),
                height=300,
                placeholder=tr("batch.topics_placeholder"),
                help=tr("batch.topics_help")
            )
            
            # Split topics by newline
            if text_input:
                # Simple split by newline, filter empty lines
                topics = [
                    line.strip() 
                    for line in text_input.strip().split('\n') 
                    if line.strip()
                ]
                
                if topics:
                    # Check count limit
                    if len(topics) > 100:
                        st.error(tr("batch.count_error", count=len(topics)))
                        topics = []
                    else:
                        st.success(tr("batch.count_success", count=len(topics)))
                        
                        # Preview topics list
                        with st.expander(tr("batch.preview_title"), expanded=False):
                            for i, topic in enumerate(topics, 1):
                                st.markdown(f"`{i}.` {topic}")
                else:
                    topics = []
            else:
                topics = []
            
            st.markdown("---")
            
            # Title prefix (optional)
            title_prefix = st.text_input(
                tr("batch.title_prefix_label"),
                placeholder=tr("batch.title_prefix_placeholder"),
                help=tr("batch.title_prefix_help")
            )
            
            # Number of scenes (unified for all videos)
            n_scenes = st.slider(
                tr("batch.n_scenes_label"),
                min_value=3,
                max_value=30,
                value=5,
                help=tr("batch.n_scenes_help")
            )
            st.caption(tr("batch.n_scenes_caption", n=n_scenes))
            
            # Config info
            st.info(f"📌 {tr('batch.config_info')}")
            
            return {
                "batch_mode": True,
                "topics": topics,
                "mode": "generate",  # Fixed to AI generate content
                "title_prefix": title_prefix,
                "n_scenes": n_scenes,
            }


def render_bgm_section(key_prefix=""):
    """Render BGM selection section"""
    with st.container(border=True):
        st.markdown(f"**{tr('section.bgm')}**")
        
        with st.expander(tr("help.feature_description"), expanded=False):
            st.markdown(f"**{tr('help.what')}**")
            st.markdown(tr("bgm.what"))
            st.markdown(f"**{tr('help.how')}**")
            st.markdown(tr("bgm.how"))
        
        # Dynamically scan bgm folder for music files (merged from bgm/ and data/bgm/)
        from pixelle_video.utils.os_util import list_resource_files
        
        try:
            all_files = list_resource_files("bgm")
            # Filter to audio files only
            audio_extensions = ('.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg')
            bgm_files = sorted([f for f in all_files if f.lower().endswith(audio_extensions)])
        except Exception as e:
            st.warning(f"Failed to load BGM files: {e}")
            bgm_files = []
        
        # Add special "None" option
        bgm_options = [tr("bgm.none")] + bgm_files
        
        # Default to "default.mp3" if exists, otherwise first option
        default_index = 0
        if "default.mp3" in bgm_files:
            default_index = bgm_options.index("default.mp3")
        
        bgm_choice = st.selectbox(
            "BGM",
            bgm_options,
            index=default_index,
            label_visibility="collapsed",
            key=f"{key_prefix}bgm_selector"
        )
        
        # BGM volume slider (only show when BGM is selected)
        if bgm_choice != tr("bgm.none"):
            bgm_volume = st.slider(
                tr("bgm.volume"),
                min_value=0.0,
                max_value=0.5,
                value=0.2,
                step=0.01,
                format="%.2f",
                key=f"{key_prefix}bgm_volume_slider",
                help=tr("bgm.volume_help")
            )
        else:
            bgm_volume = 0.2  # Default value when no BGM selected
        
        # BGM preview button (only if BGM is not "None")
        if bgm_choice != tr("bgm.none"):
            if st.button(tr("bgm.preview"), key=f"{key_prefix}preview_bgm", use_container_width=True):
                from pixelle_video.utils.os_util import get_resource_path, resource_exists
                try:
                    if resource_exists("bgm", bgm_choice):
                        bgm_file_path = get_resource_path("bgm", bgm_choice)
                        st.audio(bgm_file_path)
                    else:
                        st.error(tr("bgm.preview_failed", file=bgm_choice))
                except Exception as e:
                    st.error(f"{tr('bgm.preview_failed', file=bgm_choice)}: {e}")
        
        # Use full filename for bgm_path (including extension)
        bgm_path = None if bgm_choice == tr("bgm.none") else bgm_choice
    
    return {
        "bgm_path": bgm_path,
        "bgm_volume": bgm_volume
    }


def render_version_info():
    """Render version info and GitHub link"""
    with st.container(border=True):
        st.markdown(f"**{tr('version.title')}**")
        version = get_project_version()
        github_url = "https://github.com/AIDC-AI/Pixelle-Video"
        
        # Version and GitHub link in one line
        github_url = "https://github.com/AIDC-AI/Pixelle-Video"
        badge_url = "https://img.shields.io/github/stars/AIDC-AI/Pixelle-Video"

        st.markdown(
            f'{tr("version.current")}: `{version}` &nbsp;&nbsp; '
            f'<a href="{github_url}" target="_blank">'
            f'<img src="{badge_url}" alt="GitHub stars" style="vertical-align: middle;">'
            f'</a>',
            unsafe_allow_html=True)

