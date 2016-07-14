from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[10.6925,-19.402056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_00403-1941/sdB_KUV_00403-1941_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_00403-1941/sdB_KUV_00403-1941_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
