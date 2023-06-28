
driver.get(root_url)
time.sleep(3)
element = driver.execute_script("""return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
element.click()