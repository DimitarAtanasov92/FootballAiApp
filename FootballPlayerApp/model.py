import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

class PlayerValuePredictor:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.label_encoder = LabelEncoder()
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.prepare_data()
        self.train_model()

    def prepare_data(self):
        self.data = self.data[['wage_euro', 'overall_rating', 'potential', 'international_reputation(1-5)', 'reactions', 'composure', 'vision', 'value_euro']]
        self.data = self.data.dropna()
        self.data['international_reputation(1-5)'] = self.label_encoder.fit_transform(self.data['international_reputation(1-5)'])

    def train_model(self):
        X = self.data.drop('value_euro', axis=1)
        y = self.data['value_euro']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def predict(self, wage_euro, overall, potential, international_reputation, reactions, composure, vision):
        input_data = pd.DataFrame({
            'wage_euro': [wage_euro],
            'overall_rating': [overall],
            'potential': [potential],
            'international_reputation(1-5)': [self.label_encoder.transform([international_reputation])[0]],
            'reactions': [reactions],
            'composure': [composure],
            'vision': [vision]
        })
        return self.model.predict(input_data)[0]
