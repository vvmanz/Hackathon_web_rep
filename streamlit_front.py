import streamlit as st
import requests
import pickle
from pathlib import Path
import pandas as pd
from datetime import datetime
def show_main_content():
    st.markdown("""
        <style>
        .header {
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
            padding: 10px;
            text-align: center;
        }
        .subheader {
            color: #ffffff;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="header">Название Компании или Проекта</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Добро пожаловать в наш сервис прогнозирования стоимости авиабилетов</div>',
                unsafe_allow_html=True)

    with st.form("input_form"):
        departure_city = st.selectbox("Город вылета",
                                      ["Токио", "Сингапур", "Пекин", "Гонг Конг", "Манила", "Тайпей", "Гатвик",
                                       "Лос-Анджелес"])
        destination_city = st.selectbox("Город назначения",
                                        ["Токио", "Сингапур", "Пекин", "Гонг Конг", "Манила", "Тайпей", "Гатвик",
                                         "Лос-Анджелес"])
        departure_date = st.date_input("Дата вылета", datetime.today())
        return_date = st.date_input("Дата прилета", datetime.today())
        print(departure_date)
        print(return_date)
        submit_button = st.form_submit_button("Найти рейсы")


    if submit_button:
        departure_date_str = departure_date.strftime('%Y-%m-%d')
        return_date_str = return_date.strftime('%Y-%m-%d')

        response = requests.get(
            f'http://localhost:5000/api/flights?departure_city={departure_city}&destination_city={destination_city}&departure_date={departure_date_str}&return_date={return_date_str}')
        if response.status_code == 200:
            response_data = response.json()
            flights_data = response_data['flights']
            if flights_data:
                if response_data['alternative_results']:
                    st.info(
                        "К сожалению, на выбранные даты нет доступных рейсов. Вот все доступные авиарейсы с датой вылета, указанной вами:")
                else:
                    st.success("Найдены следующие рейсы:")

                flights_dicts = []
                for flight in flights_data:
                    flight_dict = {
                        "Город вылета": flight[1],
                        "Город назначения": flight[2],
                        "Дата вылета": flight[3],
                        "Дата прилета": flight[4],
                        "Авиакомпания": flight[5],
                        "Цена (руб)": flight[6],
                        "Источник данных": flight[7],
                        "Прогноз": "Прогноз цены"
                    }
                    flights_dicts.append(flight_dict)

                flights_df = pd.DataFrame(flights_dicts)

                for i in range(len(flights_df)):
                    row = flights_df.iloc[i]
                    st.write(row)
                    if st.button("Прогноз цены на билет:", key=f"button_{i}"):
                        st.write("Прогноз для рейса:", row["Город вылета"], "-", row["Город назначения"])

        else:
            st.error("Ошибка при получении данных")

def main():
     show_main_content()

if __name__ == "__main__":
    main()
