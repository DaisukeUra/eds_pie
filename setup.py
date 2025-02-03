from setuptools import setup, find_packages

setup(
    name='eds_pie',  # パッケージ名
    version='0.1.0',  # バージョン
    description='EDS parser',  # 説明
    packages=find_packages(),  # パッケージを自動検索
    install_requires=[  # 依存関係
        # 'dependency1',
        # 'dependency2',
    ],
    license='MIT',  # ライセンス
)
