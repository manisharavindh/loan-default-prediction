MODEL_CONFIG = {
    'architecture': {
        'layers': [128, 64, 32, 16],
        'dropout_rate': 0.3,
        'activation': 'relu',
        'output_activation': 'sigmoid'
    },
    'training': {
        'learning_rate': 0.001,
        'batch_size': 32,
        'epochs': 100,
        'validation_split': 0.2,
        'early_stopping_patience': 10
    },
    'compilation': {
        'optimizer': 'adam',
        'loss': 'binary_crossentropy',
        'metrics': ['accuracy', 'precision', 'recall']
    }
}