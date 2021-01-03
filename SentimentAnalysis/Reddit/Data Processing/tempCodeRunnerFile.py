 
                response = requests.get(f'http://finance.yahoo.com/quote/{ticker}')
                if len(response.history) == 1:
                    valid.add(ticker)
