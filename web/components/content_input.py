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
                
                # Initialize state with 8 premium "壹格专升本" video scenes
                if "fixed_scenes_count" not in st.session_state:
                    st.session_state.fixed_scenes_count = 8
                    
                    # 预设的专升本分镜旁白与自定义生图提示词
                    default_scenes = [
                        {
                            "narration": "很多 2027 届的同学公共课复习得热火朝天，但一提到专业课，脑子里却是一片空白。专业课到底选哪科？该怎么备考？这关如果搞错了，后面的努力可能全部白费！",
                            "prompt": "A frustrated male college student sitting at a desk with towering stacks of books, a glowing big neon question mark above his head, modern minimalist illustration style, deep navy and energetic orange colors, high contrast, clean lines, cinematic lighting --ar 9:16"
                        },
                        {
                            "narration": "专升本专业课总分 150 分。江西专升本将专业课划分成了 9 大招考类别，你的专科专业决定了你能报的类别，而类别直接锁定了你下午要考的专业课科目。",
                            "prompt": "An abstract 3D infographic showing a flowchart branch splitting into colorful glowing modules, representing academic disciplines, corporate pastel gradient colors, high-tech minimalism, hyper-detailed rendering --ar 9:16"
                        },
                        {
                            "narration": "比如计算机专业属于理工类，专业课要考高等数学；会计或市场营销属于管理类，专业课考管理学。同一个大类底下的所有专业，考的都是同一张专业课试卷。",
                            "prompt": "Split-screen concept, left side showing mathematical integration equations on a modern laptop screen, right side showing a colorful conceptual business organization chart, vibrant technology aesthetic, vector graphics style --ar 9:16"
                        },
                        {
                            "narration": "公共课 300 分是你的“入场券”，不过省控线，专业课再高也白搭；但专业课 150 分，才是高分段选手拉开差距、决定你能不能上公办本科的“终极杀手锏”。",
                            "prompt": "A glowing cosmic scale balance, a heavy foundational block on the left representing base entry ticket, and a shining golden laurel crown on the right representing extreme competitive advantage, surreal vector style --ar 9:16"
                        },
                        {
                            "narration": "对于理工类考生，高等数学就是一座大山。微积分作为绝对核心占了大部分分值。基础薄弱的同学，从现在起就得从函数、极限老老实实补起，绝不能拖延！",
                            "prompt": "A dynamic silhouette of a climber climbing up a steep stylized mountain built from mathematical formulas and calculus integral symbols, golden sunrise lighting, conceptual vector art, motivating style --ar 9:16"
                        },
                        {
                            "narration": "而管理学虽然理论庞杂，但体系极其清晰。最好的复习武器就是思维导图。只要把每章的核心框架理顺，专业课拿分反而比高数更加稳当、更有性价比。",
                            "prompt": "Close up of hands drawing a beautifully structured mind-map on an iPad screen, branches glowing with soft pastel light, organized concept, bright modern desk environment, flat lay view, warm aesthetic --ar 9:16"
                        },
                        {
                            "narration": "2027 届现在要做三件事：第一，通过专业对照表确定你的招考类别；第二，翻出前一年的官方大纲建立预期；第三，诚实评估底子，把专业课提前列入规划！",
                            "prompt": "A beautifully styled study planner notebook on a clean desk, three bright green checklists marked done, a cup of coffee nearby, soft volumetric window light, minimal cozy study aesthetic --ar 9:16"
                        },
                        {
                            "narration": "硬实力来自于每天有规划的积累，而不是考前三个月的盲目突击。关注我，持续为你更新 2027 届专升本最靠谱的避坑攻略，留言告诉我你想考哪门！",
                            "prompt": "A winding scenic road leading towards a bright horizon with ascending glowing arrows in the sky, minimalist modern design, warm comforting color scheme, welcoming and hopeful mood --ar 9:16"
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

