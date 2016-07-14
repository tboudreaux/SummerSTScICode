from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[196.006625,27.286778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_13016+2733/sdB_KUV_13016+2733_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_13016+2733/sdB_KUV_13016+2733_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
