from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[33.30175,-50.0777],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_JL_286/sdB_JL_286_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_JL_286/sdB_JL_286_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
