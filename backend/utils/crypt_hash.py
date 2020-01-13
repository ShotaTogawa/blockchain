import hashlib
import json


def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    # 引数の順番が変わっても実行結果が同じになるようにsortをかける
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    print(f"args: {stringified_args}")
    joined_data = "".join(stringified_args)
    print(f"joined_dat: {joined_data}")
    return hashlib.sha256(joined_data.encode("utf-8")).hexdigest()


def main():
    print(f"crypto_hash('1',2,[3]): {crypto_hash('1',2,[3])}")
    print(f"crypto_hash(2, '1',[3]): {crypto_hash(2, '1', [3])}")


if __name__ == "__main__":
    main()
