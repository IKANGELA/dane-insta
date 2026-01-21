import pandas as pd  
import matplotlib.pyplot as plt  
plt.rcParams["figure.figsize"] = (10, 5) #Importuję dane i ustawiam rozmiar wykresów
# 1. Wczytuję dane
print("=== 1. WCZYTANIE DANYCH ===")
df = pd.read_csv(r"D:\Kursy ITP Rozwój\Projekty\dane insta\Instagram_Analytics.csv")  # wczytuję dane z pliku CSV do DataFrame
print(df.head())  # wyświetlam pierwszych 5 wierszy danych

# 2. Podstawowe informacje
print("\n=== 2. PODSTAWOWE INFORMACJE O DANYCH ===")
df.info()  # wyświetlam informacje o DataFrame

print("\n=== 3. STATYSTYKI OPISOWE ===")
print(df.describe())  # wyświetlam statystyki opisowe danych

print("\n=== 4. BRAKI DANYCH ===")
print(df.isna().sum())  # sprawdzam liczbę brakujących wartości w każdej kolumnie

# 3. Konwersja daty
print("\n=== 5. KONWERSJA DATY I CZYSZCZENIE ID ===")
df['upload_date'] = pd.to_datetime(df['upload_date'], errors='coerce')  # konwertuję kolumnę 'upload_date' na format daty

df = df.dropna(subset=['post_id'])  # usuwam wiersze z brakującymi wartościami w kolumnie 'post_id'
df = df[df['post_id'].duplicated() == False]  # usuwam duplikaty w kolumnie 'post_id'

# 4. Sprawdzenie błędów reach > impressions
print("\n=== 6. REKORDY Z reach > impressions ===")
reach_errors = df[df['reach'] > df['impressions']]
print(f"Liczba rekordów reach > impressions: {len(reach_errors)}")
print(reach_errors.head())

# 5. Własny engagement rate
print("\n=== 7. OBLICZANIE WŁASNEGO ENGAGEMENT RATE ===")
df['eng_calculated'] = (df['likes'] + df['comments'] + df['shares'] + df['saves']) / df['impressions']  # obliczam wskaźnik zaangażowania
df['diff'] = df['engagement_rate'] - df['eng_calculated']  # różnica między źródłową kolumną a moją

print("\nOpis statystyczny różnic 'diff':")
print(df['diff'].describe())

# 6. Data bez czasu
print("\n=== 8. TWORZENIE KOLUMNY 'date' BEZ GODZINY ===")
df['date'] = df['upload_date'].dt.date  # godzina jest sztuczna, więc bierę tylko dzień
print(df.info())
print(df.head(20))

# 7. Ponownie liczba błędnych rekordów reach > impressions (dla pewności)
print("\n=== 9. PODSUMOWANIE: ILE MAMY reach > impressions? ===")
print((df['reach'] > df['impressions']).sum())

# Lista kolumn numerycznych do histogramów
num_cols = ['likes', 'comments', 'shares', 'saves', 'reach', 'impressions', 'engagement_rate']
df['eng_calculated'] = df['eng_calculated'].round(2)
df['diff'] = df['diff'].round(2)
df['engagement_rate'] = df['engagement_rate'].round(2)


