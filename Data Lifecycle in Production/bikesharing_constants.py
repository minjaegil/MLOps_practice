
# Features with string data types that will be converted to indices
CATEGORICAL_FEATURE_KEYS = [
    'Functioning Day', 'Holiday', 'Seasons'
]
# Numerical features that are marked as continuous
NUMERIC_FEATURE_KEYS = ['Humidity(%)', 'Rainfall(mm)', 'Snowfall (cm)', 'Solar Radiation (MJ/m2)', 'Temperature(°C)', 'Visibility (10m)', 'Wind speed (m/s)']
# Feature that can be grouped into buckets
BUCKET_FEATURE_KEYS = ['Hour']
# Number of buckets used by tf.transform for encoding each bucket feature.
FEATURE_BUCKET_COUNT = {'Hour': 4}
# Feature that the model will predict
LABEL_KEY = 'Rented Bike Count'

# Utility function for renaming the feature
def transformed_name(key):
    return key + '_xf'
