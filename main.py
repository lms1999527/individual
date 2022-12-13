import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import json
import requests
import base64

#add background image
def add_bg_from_local(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('aaa.jpg')


#Download
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

#Header

Header = st.title('Visualized Pisa Score')
st.write("Want more PISA resource? Check out this link.(https://www.oecd.org/pisa/aboutpisa.htm#:~:text=PISA%20(Programme%20for%20International%20Student,students%20in%20participating%20countries%2Feconomies.)")

#read & drop data
readdata = pd.read_csv('Pisa.csv')
readdata = readdata.drop(columns=['2013 [YR2013]'])
readdata = readdata.drop(columns=['2014 [YR2014]'])

print(readdata['2015 [YR2015]'].replace('..', np.nan, inplace=True))
print(readdata.dropna(inplace=True))

# country select
selectcon = st.sidebar.multiselect(
    'Which countries do you want to include',
    options=readdata["Country Name"].unique(),
    default=["United States"])

mask=readdata["Country Name"].isin(selectcon)
readdata=readdata[mask]

#map
fig = px.choropleth(readdata, locations="Country Code",
                    color="Country Name",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Global Map")
fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)'
})
st.plotly_chart(fig)


st.sidebar.markdown("---")


st.sidebar.write('Chose subjects here')
subject = st.sidebar.radio(
    "Select a subject: ",
    key="radio_1",
    options=["Mathmatics","Reading","Science","All"]
)


if subject == "Mathmatics":
    c = readdata
    mask = c["Series Code"].str.contains("LO.PISA.MAT")
    c = c[mask]
elif subject == "Reading":
    c = readdata
    mask = c["Series Code"].str.contains("LO.PISA.REA")
    c = c[mask]
elif subject == "Science":
    c = readdata
    mask = c["Series Code"].str.contains("LO.PISA.SCI")
    c = c[mask]
else:
    c = readdata


fig = px.histogram(c, x="Series Name", y='2015 [YR2015]',
             color='Country Name', barmode='group',
             height=400,title="2015 PISA Score/Subject")
fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)'
})
st.plotly_chart(fig)
fig2 = px.sunburst(c, path=['Series Name','Country Name'], values='2015 [YR2015]',title="2015 PISA Score/Subject")
fig2.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)'
})
st.plotly_chart(fig2)

csv = convert_df(c)
st.download_button(
   "Press to download data",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)

st.sidebar.markdown("---")


st.sidebar.write('Chose Gender here')
gender = st.sidebar.multiselect(
    "Select Gender",
    ["Male","Female"],
    ["Male","Female"]
)

if gender.__contains__("Male"):
    if gender.__contains__("Female"):
        d = readdata
        fig = px.histogram(d, x="Series Name", y='2015 [YR2015]',
                           color='Country Name', barmode='group',
                           height=400,
                           title="2015 PISA Score/Gender")
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)'
        })
        st.plotly_chart(fig)
        fig2 = px.sunburst(d, path=['Series Name', 'Country Name'], values='2015 [YR2015]',title="2015 PISA Score/Gender")
        fig2.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)'
        })
        st.plotly_chart(fig2)
        csv = convert_df(d)
        st.download_button(
            "Press to download data",
            csv,
            "file-gender.csv",
            "text/csv",
            key='download-csv-gender'
        )
    else:
        d = readdata
        mask = d["Series Name"].str.contains("Male")
        d = d[mask]
        fig = px.histogram(d, x="Series Name", y='2015 [YR2015]',
                           color='Country Name', barmode='group',
                           height=400,title="2015 PISA Score/Gender")
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)'
        })
        st.plotly_chart(fig)
        fig2 = px.sunburst(d, path=['Series Name', 'Country Name'], values='2015 [YR2015]',title="2015 PISA Score/Gender")
        fig2.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)'
        })
        st.plotly_chart(fig2)
        csv = convert_df(d)
        st.download_button(
            "Press to download data",
            csv,
            "file-gender.csv",
            "text/csv",
            key='download-csv-gender'
        )

elif gender.__contains__("Female"):
    if gender.__contains__("Male"):
        d = readdata
        fig = px.histogram(d, x="Series Name", y='2015 [YR2015]',
                           color='Country Name', barmode='group',
                           height=400,title="2015 PISA Score/Gender")
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)'
        })
        st.plotly_chart(fig)
        fig2 = px.sunburst(d, path=['Series Name', 'Country Name'], values='2015 [YR2015]',title="2015 PISA Score/Gender")
        fig2.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)'
        })
        st.plotly_chart(fig2)
        csv = convert_df(d)
        st.download_button(
            "Press to download data",
            csv,
            "file-gender.csv",
            "text/csv",
            key='download-csv-gender'
        )
    else:
        d = readdata
        mask = d["Series Name"].str.contains("Female")
        d = d[mask]
        fig = px.histogram(d, x="Series Name", y='2015 [YR2015]',
                           color='Country Name', barmode='group',
                           height=400,title="2015 PISA Score/Gender")
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)'
        })
        st.plotly_chart(fig)
        fig2 = px.sunburst(d, path=['Series Name', 'Country Name'], values='2015 [YR2015]',title="2015 PISA Score/Gender")
        fig2.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)'
        })
        st.plotly_chart(fig2)
        csv = convert_df(d)
        st.download_button(
            "Press to download data",
            csv,
            "file-gender.csv",
            "text/csv",
            key='download-csv-gender'
        )

else:
    st.error("Please Choose one!")

csv = convert_df(readdata)
st.download_button(
    "Press to download full data",
    csv,
    "fulldata.csv",
    "text/csv",
    key='download-csv-fulldata'
)