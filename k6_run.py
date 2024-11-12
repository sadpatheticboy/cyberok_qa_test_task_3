import subprocess


def run_k6_test():
    result = subprocess.run(["k6", "run", "k6.js"], capture_output=True, text=True)

    if result.returncode != 0:
        print("Ошибка при выполнении k6 теста:")
        print(result.stderr)
        return

    print("Результаты нагрузочного тестирования:")
    print(result.stdout)



if __name__ == "__main__":
    run_k6_test()