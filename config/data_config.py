DATA_CONFIG = {
    'file_paths': {
        'raw_data': '',
        'processed_data': '',
        'train_data': '',
        'test_data': ''
    },
    'preprocessing': {
        'train_split': 0.7,
        'val_split': 0.15,
        'test_split': 0.15,
        'random_state': 42,
        'target_column': '',
        'categorical_columns': ['', '', ''],
        'numerical_columns': ['', '', ''],
        'drop_columns': ['', '']
    },
    'feature_engineering': {
        'create_ratios': True,
        'scale_features': True,
        'handle_outliers': True,
        'outlier_method': 'iqr'
    }
}
