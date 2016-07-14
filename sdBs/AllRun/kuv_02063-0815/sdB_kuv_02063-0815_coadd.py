from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[32.189333,-8.016581],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_02063-0815/sdB_kuv_02063-0815_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_02063-0815/sdB_kuv_02063-0815_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
