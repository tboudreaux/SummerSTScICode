from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[135.998667,37.671892],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_09008+3752/sdB_KUV_09008+3752_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_09008+3752/sdB_KUV_09008+3752_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
