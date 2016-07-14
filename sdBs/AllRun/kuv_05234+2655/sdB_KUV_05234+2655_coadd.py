from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[81.617792,26.960639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_05234+2655/sdB_KUV_05234+2655_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_05234+2655/sdB_KUV_05234+2655_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
