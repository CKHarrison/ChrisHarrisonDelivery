from package import Package, create_package_table


if __name__ == '__main__':
    package_hash = create_package_table()
    print(package_hash.print())
