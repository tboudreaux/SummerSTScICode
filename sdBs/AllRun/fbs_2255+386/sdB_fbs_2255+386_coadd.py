from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[344.499667,38.860778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2255+386/sdB_fbs_2255+386_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2255+386/sdB_fbs_2255+386_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
