# Binary

```shell
cd a_src/
python3 -m nuitka --follow-imports --module --no-prefer-source-code core.py
mv core*.so ../a/
```

```shell
cd b_src/
python3 -m nuitka --follow-imports --module --no-prefer-source-code core.py
mv core*.so ../b/
```

```shell
python3 -m nuitka --follow-imports --standalone --no-prefer-source-code main3.py

./main3.dist/main3
```

