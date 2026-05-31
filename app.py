import streamlit as st
from pathlib import Path
from html import escape

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(
    page_title="나의 웹사이트 연결고리",
    page_icon="🔗",
    layout="wide"
)

# -----------------------------
# CSS 디자인
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #f8fafc;
}

.main-title {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 10px;
    color: #111827;
}

.sub-title {
    text-align: center;
    font-size: 16px;
    color: #4b5563;
    margin-bottom: 35px;
}

.link-card {
    background-color: #ffffff;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
    margin-bottom: 18px;
    border: 1px solid #eeeeee;
}

.link-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 8px;
    color: #111827;
}

.link-desc {
    font-size: 15px;
    color: #374151;
    margin-bottom: 16px;
    line-height: 1.6;
}

a.custom-button {
    display: block;
    text-align: center;
    background-color: #2563eb;
    color: white !important;
    padding: 13px 18px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 700;
    font-size: 16px;
}

a.custom-button:hover {
    background-color: #1d4ed8;
}

.download-panel {
    background-color: #ffffff;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
    border: 1px solid #eeeeee;
    margin-bottom: 18px;
}

.download-title {
    font-size: 22px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 8px;
}

.download-desc {
    font-size: 14px;
    color: #374151;
    line-height: 1.6;
    margin-bottom: 8px;
}

.download-small {
    font-size: 12px;
    color: #6b7280;
    line-height: 1.5;
}

.section-title {
    font-size: 24px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 14px;
}

.file-missing {
    background-color: #fff1f2;
    border: 1px solid #fecdd3;
    border-radius: 12px;
    padding: 10px;
    color: #9f1239;
    font-size: 13px;
    margin-bottom: 10px;
}

.footer-text {
    text-align: center;
    color: #6b7280;
    font-size: 13px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 제목 부분
# -----------------------------
st.markdown(
    '<div class="main-title">🔗 나의 웹사이트 연결고리</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-title">아래 버튼을 누르면 원하는 웹사이트로 이동할 수 있습니다.</div>',
    unsafe_allow_html=True
)

# -----------------------------
# 링크 목록
# -----------------------------
links = [
    {
        "title": "(⭐최종 분석⭐)📊 2025-03-01 ~ 2026-02-28 전국 학교 실제 학사일정 vs GA 최적 학사일정 차이 분석 결과 바로보기",
        "description": "분량으로 인해 ppt에 담지 못한 마지막 분석입니다!! 꼭 봐주세요!! 실제와 최적화 알고리즘이 짠 학사일정을 비교하면서 학사일정이 학교의 업무효율성을 고려하는지? 학새의 학업능력을 고려하는지? 결론을 냅니다!!",
        "url": "https://ga-vs-real-differnce-analysis-result.streamlit.app/"
    },
    {
        "title": "+더 많은 학사일정 다운받기+",
        "description": "위 사이트에서 다운받은 학사일정만 사용 가능합니다.",
        "url": "https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17220190722175038389180&infSeq=3&cateId=A0005"
    },
    {
        "title": "(streamlit 데이터 용량 제한으로 아마 안될듯, 로컬이용강추👍) 📚 학사일정 기반 학습 공백 위험지수 대시보드",
        "description": "위 데이터를 다운받으시고, 업로드하면 결과를 보실 수 있습니다. 또한 다른기간의 학사일정을 다운로드 받아도 분석 가능합니다.",
        "url": "https://schedule-blank-risk.streamlit.app/"
    },
    {
        "title": "📚 2025-03-01 ~ 2026-02-28 학사일정 기반 학습 공백 위험지수 결과 바로보기",
        "description": "위 데이터의 다운로드 없이 주제로 정한 기간의 결과를 바로 보실 수 있습니다.",
        "url": "https://schedule-blank-risk-oneshow.streamlit.app/"
    }
    ,
    {
        "title": "전국 학교 망각 위험지수 지도",
        "description": "전국 학교의 망각 위험지수를 지도에 표시하였습니다.",
        "url": "https://forget-risk-map.streamlit.app/"
    },
    {
        "title": "(streamlit 데이터 용량 제한으로 아마 안될듯, 로컬이용강추👍) 🧬 전국 학교 실제 학사일정 vs GA 최적 학사일정 차이 분석",
        "description": "위 데이터를 다운받으시고, 업로드하면 결과를 보실 수 있습니다. 또한 다른기간의 학사일정을 다운로드 받아도 분석 가능합니다.",
        "url": "https://ga-vs-real-difference-analysis.streamlit.app/"
    }
    
    
    
    
]

# -----------------------------
# 다운로드 파일 목록
# 파일명 정확히 확인:
# files/school_schedule.zip
# files/schedule_blank_risk_local.zip
# files/GAvsREAL_difference_analysis_local.zip
# -----------------------------
download_files = [
    {
        "label": "📁 학사일정 원본 데이터",
        "description": "분석에 사용한 월별 학사일정 CSV 파일을 압축한 자료입니다.",
        "path": "files/school_schedule.zip",
        "file_name": "school_schedule.zip"
    },
    {
        "label": "📚 학습 공백 위험지수 대시보드 로컬 실행 파일",
        "description": "웹 배포에서 정상 작동하지 않을 경우, 이 파일을 내려받아 로컬 컴퓨터에서 실행할 수 있습니다.",
        "path": "files/schedule_blank_risk_local.zip",
        "file_name": "schedule_blank_risk_local.zip"
    },
    {
        "label": "🧬 GA 차이 분석 사이트 로컬 실행 파일",
        "description": "전국 학교 실제 학사일정과 GA 최적 학사일정 차이 분석 사이트를 로컬에서 실행할 수 있는 파일입니다.",
        "path": "files/GAvsREAL_difference_analysis_local.zip",
        "file_name": "GAvsREAL_difference_analysis_local.zip"
    }
]

# -----------------------------
# 왼쪽 다운로드 / 오른쪽 사이트 연결 영역
# -----------------------------
left_col, main_col = st.columns([1, 2.4], gap="large")

with left_col:
    st.markdown("""
    <div class="download-panel">
        <div class="download-title">📦 다운로드 자료</div>
        <div class="download-desc">
            웹에서 정상 작동하지 않을 경우 아래 파일을 내려받아 로컬에서 실행할 수 있습니다.
        </div>
        <div class="download-small">
            ※ 압축 파일을 푼 뒤, 폴더 안의 안내에 따라 실행하면 됩니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    for item in download_files:
        st.markdown(
            f"""
            <div class="download-panel">
                <div class="download-title">{escape(item["label"])}</div>
                <div class="download-desc">{escape(item["description"])}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        file_path = Path(item["path"])

        if file_path.exists():
            st.download_button(
                label=f"다운로드",
                data=file_path.read_bytes(),
                file_name=item["file_name"],
                mime="application/zip",
                use_container_width=True,
                key=f"download_{item['file_name']}"
            )
        else:
            st.markdown(
                f"""
                <div class="file-missing">
                    파일을 찾지 못했습니다.<br>
                    확인 경로: {escape(item["path"])}
                </div>
                """,
                unsafe_allow_html=True
            )

with main_col:
    st.markdown('<div class="section-title">🌐 웹사이트 바로가기</div>', unsafe_allow_html=True)

    for link in links:
        title = escape(link["title"])
        description = escape(link["description"])
        url = escape(link["url"], quote=True)

        st.markdown(
            f"""
            <div class="link-card">
                <div class="link-title">{title}</div>
                <div class="link-desc">{description}</div>
                <a class="custom-button" href="{url}" target="_blank">
                    이동하기
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------
# 아래 안내 문구
# -----------------------------
st.markdown("---")
st.markdown(
    '<div class="footer-text">QR 코드를 통해 접속한 뒤 원하는 버튼을 눌러 이동할 수 있습니다.</div>',
    unsafe_allow_html=True
)
