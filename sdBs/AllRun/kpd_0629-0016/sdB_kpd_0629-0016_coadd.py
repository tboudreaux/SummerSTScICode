from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[97.974208,0.320206],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kpd_0629-0016/sdB_kpd_0629-0016_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kpd_0629-0016/sdB_kpd_0629-0016_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
