'use client'
import Navbar from './navbar'

export default function Main() {
    return (
    <div className="w-screen h-[3250px] bg-black">
        <Navbar></Navbar>  
        <div className="w-full h-[900px] bg-cover bg-top bg-no-repeat bg-[url('/bot2.jpeg')] opacity-40">
        </div>
        <div className='absolute text-white top-[225px] left-[100px] text-8xl font-bold w-[85%] h-[50px] flex flex-col items-start opacity-100'>
          Introducing crisisvision.
          <span className="text-wrap text-5xl text-[#EB5E28]">surveying the world's most dangerous frontiers</span>
        </div>
  
      <div className="text-white text-5xl mt-10 font-bold top-40 w-full justify-center flex">
        Use Cases
        </div>
  
      <div className='relative w-auto m-8 pt-12 h-[700px] flex justify-around'>
          <div className="relative rounded-md w-[60%] h-[560px] bg-cover bg-no-repeat bg-[url('/forestfire.jpg')]">
          </div>
          <div className='relative text-white top-40 w-[25%]'>
            <div className="text-5xl text-[#EB5E28] mb-8 justify-center text-wrap">
              Forest Fires
            </div>
              <div className="text-3xl justify-center text-wrap">
                CrisisVision can be used to survey fires and stream a live feed of the affected area.
              </div>
          </div>
      </div>
  
      <div className='relative w-[100%] mt-[100px] h-[700px] flex justify-around'>
          <div className='relative top-40 text-white w-[300px]'>
          <div className="text-5xl text-[#EB5E28] mb-8 text-wrap">
            Hurricanes
          </div>
          <div className="text-3xl text-wrap">
            CrisisVision can be used to survey hurricane damage and detect trapped individuals or animals.
          </div>
          </div>          
          <div className="relative rounded-md w-[50%] h-[560px] right-0 bg-cover bg-no-repeat bg-[url('/hurricaneaftermath.jpg')]">
        </div>
      </div>
      
      <div className='relative w-auto m-8 pt-12 h-[500px] flex justify-around'>
          <div className="relative rounded-md w-[60%] h-[560px] bg-cover bg-no-repeat bg-[url('/warzone.avif')]">
          </div>
          <div className='relative text-white top-40 w-[25%]'>
            <div className="text-5xl text-[#EB5E28] mb-8 justify-center text-wrap">
              Warzones
            </div>
              <div className="text-3xl justify-center text-wrap">
                CrisisVision can be used as a first contact in warzones to survey the area and detect any potential threats without risking individuals.
              </div>
          </div>
      </div>
  
      </div>
    );
  }