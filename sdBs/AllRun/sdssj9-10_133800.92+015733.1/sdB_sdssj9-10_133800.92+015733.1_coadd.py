from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[204.503833,1.959194],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_133800.92+015733.1/sdB_sdssj9-10_133800.92+015733.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_133800.92+015733.1/sdB_sdssj9-10_133800.92+015733.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
