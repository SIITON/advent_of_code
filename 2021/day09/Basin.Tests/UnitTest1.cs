using NUnit.Framework;

namespace Basin.Tests
{
    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Can_Get_Pixel()
        {
            // kasta in en etta, få data[0][0] = 1 returnerar 1. 0 en nolla.
            Assert.Pass();
        }

        [Test]
        public void Can_Get_Neighbors()
        {
            // 1 0 
            // 0 0 
            // returnerar 1.
            Assert.Pass();
        }

        [Test]
        public void Can_Get_Neighbors2()
        {
            // 1 0 
            // 1 0 
            // returnerar 2.
            Assert.Pass();
        }
    }
}