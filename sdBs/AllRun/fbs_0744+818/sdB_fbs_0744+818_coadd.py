from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[118.4615,81.697583],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0744+818/sdB_fbs_0744+818_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0744+818/sdB_fbs_0744+818_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
