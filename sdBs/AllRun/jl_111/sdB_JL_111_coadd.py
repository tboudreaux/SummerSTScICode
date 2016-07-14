from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[339.594167,-76.878517],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_JL_111/sdB_JL_111_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_JL_111/sdB_JL_111_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
