
"""
# Configurez le runner HTMLTestRunner
    runner = HTMLTestRunner(
        report_filepath="my_report.html",
        title="My unit test",
        description="This demonstrates the report output by HTMLTestRunner.",
        open_in_browser=True
    )
    # Exécutez uniquement le test ajouté à la suite
    runner.run(my_test_suite())
    
Vérifiez si le dossier 'test-reports' existe, sinon créez-le
    report_path = 'test-reports'
    os.makedirs(report_path, exist_ok=True)
    print(f"Les rapports seront générés dans : {os.path.abspath(report_path)}")

    try:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=report_path),
            failfast=False, buffer=False, catchbreak=False
        )
        # Vérifiez si les fichiers XML sont créés
        if os.path.exists(report_path):
            print(f"Le dossier de rapport a été créé : {report_path}")
            print(f"Fichiers générés : {os.listdir(report_path)}")
        else:
            print("Le dossier de rapport n'a pas été créé.")
    except Exception as e:
        print(f"Erreur lors de l'exécution des tests : {e}")
# logging.basicConfig(stream=sys.stderr)
# logging.getLogger("DummyLogger").setLevel(logging.INFO)
# unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='outputFolder', report_title='Dummy report title test'))
"""
