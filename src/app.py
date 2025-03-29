import streamlit as st


import currencies

from main import get_exchange_rate, convert_currency

st.title(' :dollar: Currency Convertor')
st.markdown("""
            This tool allows you to convert amounts between different currencies.
            Just Enter the amount and choose the currencies to see the results.
            """) 
currencies= list(currencies.MONEY_FORMATS.keys())

base_currency = st.selectbox('From currency (Base):', currencies)
target_currency = st.selectbox('To currency (Target):', currencies)
amount = st.number_input('Enter amount:', min_value=0.0)

exchange_rate = get_exchange_rate(base_currency, target_currency)

# Ensure that the exchange_rate is a float and not a function
if exchange_rate is not None:
    converted_amount = convert_currency(amount, exchange_rate)
    st.write(f"{amount} {base_currency} is {converted_amount} {target_currency}")
else:
    st.error(f"Could not retrieve exchange rate for {base_currency} to {target_currency}.")


if amount > 0 and base_currency and target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        st.success(f"✅ Exchange Rate: {exchange_rate:.4f}")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Base Currency", value=f"{amount:.2f} {base_currency}")
        col2.markdown("<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="Target Currency", value=f"{converted_amount:.2f} {target_currency}")
    else:
        st.error('Error fetching exchange rate.')


st.markdown("---")
st.markdown("### ℹ️ About This Tool")
st.markdown("""
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
- The conversion updates automatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press a button!
""")
