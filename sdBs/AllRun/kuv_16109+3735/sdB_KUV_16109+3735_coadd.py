from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[243.181,37.45085],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_16109+3735/sdB_KUV_16109+3735_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_16109+3735/sdB_KUV_16109+3735_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
