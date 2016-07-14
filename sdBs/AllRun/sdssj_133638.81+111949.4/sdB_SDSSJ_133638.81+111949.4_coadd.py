from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[204.161708,11.330389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_133638.81+111949.4/sdB_SDSSJ_133638.81+111949.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_133638.81+111949.4/sdB_SDSSJ_133638.81+111949.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()