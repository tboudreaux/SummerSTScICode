from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[241.921917,25.705639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_160741.26+254220.3/sdB_sdssj9-10_160741.26+254220.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_160741.26+254220.3/sdB_sdssj9-10_160741.26+254220.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
