# AssertJ Migrater

This is an simple script which will change JUnits assertEqual, assertNull, assertTrue, assertFalse, assertNotNull
to assertThat assertions from AssertJ.

Run with `python3 assertJMigrater.py`

Lets say you have an file under /home/DeveloperX/dev/projectX/test.java

After you start the script you will be asked to enter an absolute path to your testfile like the one above.

 
It could look like this:

```java
public void whenA_thenB(){
    assertEquals(test, test);
    assertNotNull(test.get());
    assertNull(test.get(123));
    assertTrue(test.get(dsf.grz()));
    assertFalse(test.get(123).get());
}
```

and will be turned into this:

```java
public void whenA_thenB(){
    assertThat(test).isEqualTo(test);
    assertThat(test.get()).isNotNull();
    assertThat(test.get(123)).isNull();
    assertThat(test.get(dsf.grz())).isTrue();
    assertThat(test.get(123).get()).isFalse();
}
```