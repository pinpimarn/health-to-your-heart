import pandas as pd
import matplotlib.pyplot as plt


class DataAnalytic:
    '''Analyse all of the data.'''

    def __init__(self):
        self.data = pd.read_csv('heart_2020_cleaned.csv')

    def get_columns(self):
        lst = []
        for col in self.data.columns:
            if col != 'BMI':
                lst.append(col)
        return lst


class ChartPlot:

    def basic_plot(self, df, column, chart_type):
        if chart_type == 'pie':
            df.value_counts(column).plot(y=column, kind=chart_type, legend=True, title='Data Result', autopct='%1.1f%%')
        else:
            df.value_counts(column).plot(y=column, kind=chart_type, title='Data Result')
        plt.show(block=True)

    def double_plot(self, df, column, chart_type):
        if chart_type == 'pie':
            df[df.HeartDisease == 'Yes'].value_counts(column).plot(
                ylabel=column, y=column, kind=chart_type, title='Heart Disease Count', autopct='%1.2f%%')
        else:
            df[df.HeartDisease == 'Yes'].value_counts(column).plot(
                ylabel=column, y=column, kind=chart_type, title='Heart Disease Count')
        plt.show(block=True)
