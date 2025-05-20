import yfinance as yf
import matplotlib.pyplot as plt


ibm = yf.download('IBM', start='2020-01-01', end='2023-01-01')
tesla = yf.download('TSLA', start='2020-01-01', end='2023-01-01')

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(ibm.index, ibm['Close'])
plt.title('Ações da IBM')
plt.ylabel('Preço ($)')
plt.subplot(2, 1, 2)
plt.plot(tesla.index, tesla['Close'], 'r')
plt.title('Ações da Tesla')
plt.ylabel('Preço ($)')
plt.tight_layout()
plt.show()