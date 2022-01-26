from application_logging import logger
import data_loader
from Processing import data_preprocessing
from sklearn.model_selection import train_test_split
from best_model_finder import tuner
from File_Operation.file_op import File_Operation


class Training_model:
    def __init__(self):
        self.log_writer = logger.App_Logger()
        self.file_object = open("Training_Logs/ModelTrainingLog.txt", 'a+')


    def train_model(self):
        # Logging the start of Training
        self.log_writer.log(self.file_object, 'Start of Training')
        try:
            # Getting the data from the source
            data_getter = data_loader.Data_Getter(self.file_object, self.log_writer)
            data = data_getter.get_data()

            """doing the data preprocessing"""
            preprocess=data_preprocessing()
            data=preprocess.outier_treatment(data)
            data=preprocess.scaling_of_numcol(data)
            data=preprocess.encode_categorical_col(data)

            X,Y=preprocess.separate_label_feature(self, data, label_column_name='expenses')

            x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=1 / 3,
                                                            random_state=42)

            model_finder = tuner.Model_Finder()  # object initialization

            # getting the best model for each of the clusters
            best_model_name, best_model = model_finder.get_best_model(x_train, y_train, x_test, y_test)

            # saving the best model to the directory.

            file_op = File_Operation(self.file_object)
            save_model = file_op.save_model(best_model, best_model_name )

            # logging the successful Training
            self.log_writer.log(self.file_object, 'Successful End of Training')
            self.file_object.close()

        except Exception as e:
            # logging the unsuccessful Training
            self.log_writer.log(self.file_object, 'Unsuccessful End of Training')
            self.file_object.close()
            raise Exception









































