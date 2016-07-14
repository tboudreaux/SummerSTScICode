from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[23.47425,-19.744306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_0131-2000/sdB_MCT_0131-2000_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_0131-2000/sdB_MCT_0131-2000_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
