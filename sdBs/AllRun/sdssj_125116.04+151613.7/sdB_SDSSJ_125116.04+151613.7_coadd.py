from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[192.816833,15.270472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_125116.04+151613.7/sdB_SDSSJ_125116.04+151613.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_125116.04+151613.7/sdB_SDSSJ_125116.04+151613.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
