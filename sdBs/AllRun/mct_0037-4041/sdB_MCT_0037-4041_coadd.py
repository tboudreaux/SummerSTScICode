from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[10.027208,-40.415458],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_0037-4041/sdB_MCT_0037-4041_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_0037-4041/sdB_MCT_0037-4041_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
