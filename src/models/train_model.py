from regressor import train_model_ridge,train_random_forest,train_model_with_grid_search


def run_regressor():
	sales_model = train_model_ridge(pandas.read_csv(DataPreProcessing().output().path))
        with open(self.output().path, 'wb') as f:
            pickle.dump(sales_model,f )
        request = Request('http://127.0.0.1:5000/loadModels/')
        try:
            print "Reloading models"
            response = urlopen(request)
        except URLError, e:
            "No Roseman Sales Prediction API", e