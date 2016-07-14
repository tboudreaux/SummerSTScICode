from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[322.275125,0.752556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_212906.03+004509.2/sdB_sdssj_212906.03+004509.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_212906.03+004509.2/sdB_sdssj_212906.03+004509.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
