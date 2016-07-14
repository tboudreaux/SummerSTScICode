from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[8.968167,52.763706],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kpd_0033+5229/sdB_kpd_0033+5229_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kpd_0033+5229/sdB_kpd_0033+5229_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
