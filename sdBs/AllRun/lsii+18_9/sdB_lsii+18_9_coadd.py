from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[295.879958,18.410331],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lsii+18_9/sdB_lsii+18_9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lsii+18_9/sdB_lsii+18_9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
