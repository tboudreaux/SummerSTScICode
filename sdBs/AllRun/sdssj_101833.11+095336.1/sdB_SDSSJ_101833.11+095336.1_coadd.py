from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[154.637958,9.893361],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_101833.11+095336.1/sdB_SDSSJ_101833.11+095336.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_101833.11+095336.1/sdB_SDSSJ_101833.11+095336.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
