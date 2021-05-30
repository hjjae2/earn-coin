## :zap: Earn-coin

### Information

You can use below functions using My API key.

1. 자산조회
2. 주문조회
3. 주문하기

<br>

### Structure

`config/` : A package for config file<br>

`lib/` : A package for library classes (upbit, key_reader, ...)<br>

`runner/` : A package for runner classes (runner, each_runner, ...)<br>

`trader/` : A package for trader classes (trader, each_trader, ...)<br>

<br>

### Usage

**1. Install packages**
```
pip install -r requirements.txt
```

**2. Put the access.key, secret.key into `config/`**

**3. Run runner**
```
python -m runner.{coin}_runner
```

<br>

### Documents

- Upbit open API : https://upbit.com/mypage/open_api_management 

- Upbit dev center : https://docs.upbit.com/

- Upbit API references : https://docs.upbit.com/reference
